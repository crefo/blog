var toggle_comment_box;

$(document).ready(function() {

	toggle_comment_box = function(url, entry_id){
		console.log('am i called more' + entry_id);
		var el = $('#comment_box_'+entry_id);

		if(el.is(':visible')){
			el.hide();
		}
		else{
			$.ajax({
				type: "GET",
				url: url,
				success: function(data) {
					el.append(data);
					el.show();
				}
			});	
		}
    };

    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 

});