////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//   ? ???? ???? ? ?? ?????? ????????? ?????????, ??????? ????????? ? ??????, ???????????, ????-?? ????? ???? ???.
//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/**
 * ?????????? ??????????, ? ??????? ????? ????? ??????? ?????? ??????? ?????? ?? ????.
 * @field
 */

var DialogLogin = null;
var DialogRegister=null;
/***********************************************************************************************************************
 *                               "???????????" ??????? ??????? ?????? ?? ????.
 * @class CDialogLogin
 *
 **********************************************************************************************************************/

function CDialogLogin() {
    // ??????????? JQuery UI Dialog.
    this.el = $("#DialogLogin");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        modal: true,
        closeOnEscape: true,
        okOnEnter:true,
        buttons : [
            {
                text : "Login",
                width: 100,
                icons : {
                 primary : "ui-icon-check"
                },
                click: function() {
                    console.log( caller );
                    caller.really_login();
                }

            }, {
                text : "Cancel",
                width: 100,
                icons : {
                 primary : "ui-icon-circle-close"
                },
                click : function() {
                    // ??? ??????? ?? ?????? "??????" - ?????? ?? ??????????, ??????
                    // ???????? ?????? ? ???.
                    $( this ).dialog( "close" );
                }
            }
        ]
    });
}
function Register() {
    // ??????????? JQuery UI Dialog.
    this.el = $("#DialogRegister");
    var caller = this;
    this.el.dialog( {
        autoOpen: false,
        modal: true,
        closeOnEscape: true,
        buttons : [
            {
                text : "Register",
                width: 100,
                icons : {
                 primary : "ui-icon-check"
                },
                click: function() {
                    console.log( caller );
                    caller.really_register();
                }

            }, {
                text : "Cancel",
                width: 100,
                icons : {
                 primary : "ui-icon-circle-close"
                },
                click : function() {
                    // ??? ??????? ?? ?????? "??????" - ?????? ?? ??????????, ??????
                    // ???????? ?????? ? ???.
                    $( this ).dialog( "close" );
                }
            }
        ]
    });
}
/***********************************************************************************************************************
 * ????????? ??????? ??????????? ?? ??????.
 * @memberOf CDialogLogin
 **********************************************************************************************************************/

CDialogLogin.prototype.show = function () {
    // ????????? ??????? ?? ??????.
    this.el.dialog("open");
    // @todo "??????????" ????????? ???? ????????.
};

Register.prototype.show = function () {
    // ????????? ??????? ?? ??????.
    $("#DialogLogin").hide();
    this.el.dialog("open");
    // @todo "??????????" ????????? ???? ????????.
};


/***********************************************************************************************************************
 * ?????? ?? ???????????.
 * @memberOf CDialogLogin
 */


CDialogLogin.prototype.really_login = function() {
    var caller = this;
        $.ajax({ // create an AJAX call...
                data: {
                    username : $("#username").val(),
                    password : $("#password").val()
                    // $(this).serialize()
                }, // get the form data
                type: "POST", // $(this).attr('method'), // GET or POST
                dataType : "json",
                url: "/accounts/login/", // $(this).attr('action'), // the file to call
                success: function(data) { // on success..
                   // window.location = response;
                    // alert("success");
                    console.log( data );
                    if ( data.result === "true" ) {
                        caller.el.dialog( "close" );
                        document.location = "/";
                    } else {
                        console.log( data );
                        caller.el.dialog({ title : data.description });
                        // @todo ??????? ??????? ??? ????? ???????
                    }

                },
                error : function(request, status, thError ) {
                    global_error( request, status, thError );
                    console.log("on error");
                    console.log( request );
                    console.log( status );
                    console.log( thError );
                }
            });


};
Register.prototype.really_register = function() {
    var caller = this;
        $.ajax({ // create an AJAX call...
                data: $('form#Register').serialize(), // get the form data
                type: "POST", // $(this).attr('method'), // GET or POST
                dataType : "json",

                url: "/accounts/register/", // $(this).attr('action'), // the file to call
                success: function(data) { // on success..
                   // window.location = response;
                    // alert("success");

                    console.log( data );
                    if ( data.result === "true" ) {
                        caller.el.dialog( "close" );
                        document.location = "/";
                    } else {
                        console.log( data );
                        caller.el.dialog({ title : data.description });
                        // @todo ??????? ??????? ??? ????? ???????
                    }

                },
                error : function(request, status, thError ) {
                    global_error( request, status, thError );
                    console.log("on error");
                    console.log( request );
                    console.log( status );
                    console.log( thError );
                }
            });


};