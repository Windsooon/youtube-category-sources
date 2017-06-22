function get_category(url) {
	$.ajax({
		url: url,
		type: "GET",
		dataType: "json",
		success:function(data){
            $.each(data.category, function(k, v) {
                var $option = $("<option />", {
                    "value": k,
                    "text": v
                });
                $("#select-cate").append($option);
            });
        }
    });
};

function set_block() {
     var $cate_block = $("<div />", {
            "class": "pure-u-1 pure-u-md-1-3 cate-block"
        });
     var $cate_block_inside = $("<div />", {
            "class": "cate-block-inside"
        });
     var $cate_title = $("<div />", {
            "class": "cate-title"
        });
     var $cate_img = $("<img />", {
            "class": "cate-img"
        });
     var $cate_span = $("<span />", {
            "class": "cate-span",
            "text": "Degisn"
        });
    
}
