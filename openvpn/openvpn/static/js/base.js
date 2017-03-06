////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                Функция, которая обрабатывается на момент готовности DOM-модели клиента.
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
var _base=new Base();
/**
 * @class Base
 * @constructor
 */
function Base(){

}
Base.prototype.on_document_ready=function(){
    this.create_menu();
};
Base.prototype.create_menu=function(){
     $("#navigation").menu({
                position: {
                    "my": "left+5 bottom",
                    "at": "left top+80"
                },
                icons: {submenu: "ui-icon-blank"}
            });

    $("#navigation").removeClass("ui-widget").removeClass("ui-widget-content");
    $("#navigation li").each(function (item) {
        $(this).addClass("ui-widget")
               .addClass("ui-widget-content")
                .addClass("ui-widget-header");
            });

    $("ul li").unbind("mouseover");
    $("ul li").mouseover( function() {
        console.log("mouse over");
    });
    $("ul li").show( function() {
        console.log("on show")
    });
    /*
    $("ul li").popup( function() {
        console.log("on popup");
    })
    */
};
$( document ).ready(function() {
    DialogLogin = new CDialogLogin();
});
$( document).ready(function(){
    DialogRegister=new Register();
});


$( document ).ready(function() {
   $('#Logout').click(function () {
       $.ajax({
           url:"/logout/",
           cache:false,
           success:function(data){
               setTimeout(function(){window.location = window.location}, 3000);

           }
       })


    });
});
$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});
