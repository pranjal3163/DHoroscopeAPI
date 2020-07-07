var taskId;
var uniqueId;
var statusInterval;
var url;
var siteUrl = {
    1: 'http://astrology.kudosmedia.net/m/capricorn?day=',
    2: 'http://astrology.kudosmedia.net/m/aquarius?day=',
    3: 'http://astrology.kudosmedia.net/m/pisces?day=',
    4: 'http://astrology.kudosmedia.net/m/aries?day=',
    5: 'http://astrology.kudosmedia.net/m/taurus?day=',
    6: 'http://astrology.kudosmedia.net/m/gemini?day=',
    7: 'http://astrology.kudosmedia.net/m/cancer?day=',
    8: 'http://astrology.kudosmedia.net/m/leo?day=',
    9: 'http://astrology.kudosmedia.net/m/virgo?day=',
    10: 'http://astrology.kudosmedia.net/m/libra?day=',
    11: 'http://astrology.kudosmedia.net/m/scorpio?day=',
    12: 'http://astrology.kudosmedia.net/m/sagittarius?day='
};

var sunshines =["Capricorn","Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius"];
var selectedCategory;

$(document).ready(function(){
    $(document).on('click', '#start-crawl', function(){
        selectedCategory = $('#site-select option:selected').val();
        for(k in siteUrl){
            if(k === selectedCategory){
                url = siteUrl[k]
            }
        }
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is working...');
        $.ajax({
            url: '/api/crawl/',
            type: 'POST',
            data: {
                'url': url,
            },
            success: crawlSuccess,
            error: crawlFail,
        })
    });

    $(document).on('click', '#show-data', function(){
        selectedCategory = $('#site-select option:selected').val();
        $.ajax({
            url: '/api/showdata/',
            type: 'GET',
            data: {
                'sunshine': sunshines[selectedCategory - 1]
            },
            success: showData,
            error: showDataFail
        })
    });
});

function checkCrawlStatus(taskId, uniqueId){
    $.ajax({
        url: '/api/crawl/?task_id='+taskId+'&unique_id='+uniqueId+'/',
        type: 'GET',
        success: showCrawledData,
        error: showCrawledDataFail,
    })
}

function crawlSuccess(data){
    taskId = data.task_id;
    uniqueId = data.unique_id;
    statusInterval = setInterval(function() {checkCrawlStatus(taskId, uniqueId);}, 2000);
}

function crawlFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showCrawledData(data){
    if (data.status){
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is ' + data.status + ' ... ' + 'After crawling, the results are returned');
    }else{
        clearInterval(statusInterval);
        $('#progress').attr("class", "alert alert-primary");
        $('#progress').html('crawling is finished!');
        var list = data.data;
        var html = '';
        for(var i=0; i<list.length; i++){
            html += `
                <tr>
                    <th scope="row">`+ (i + 1) +`</th>
                    <td width="20%">`+ list[i].sign_name +`</td>
                    <td>`+ list[i].date_range +`</td>
                    <td>`+ list[i].current_date +`</td>
                    <td>`+ list[i].description +`</td>
                    <td>`+ list[i].compatibility +`</td>
                    <td>`+ list[i].mood +`</td>
                    <td>`+ list[i].color +`</td>
                    <td>`+ list[i].lucky_number +`</td>
                    <td>`+ list[i].lucky_time +`</td>
                </tr>
            `;
        }
        $('#board').html(html);
    }
}

function showCrawledDataFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showData(data){
    var list = data.data;
    var html = '';
    for(var i=0; i<list.length; i++){
        html += `
            <tr>
                <th scope="row">`+ (i + 1) +`</th>
                <td width="20%">`+ list[i].sign_name +`</td>
                <td>`+ list[i].date_range +`</td>
                <td>`+ list[i].current_date +`</td>
                <td>`+ list[i].description +`</td>
                <td>`+ list[i].compatibility +`</td>
                <td>`+ list[i].mood +`</td>
                <td>`+ list[i].color +`</td>
                <td>`+ list[i].lucky_number +`</td>
                <td>`+ list[i].lucky_time +`</td>
            </tr>
        `;
    }
    $('#progress').attr("class", "");
    $('#progress').empty();
    $('#board').html(html);
}

function showDataFail(data){
    $('#progress').attr("class", "alert alert-danger");
    $('#progress').html(data.responseJSON.error);
    $('#board').empty();
}