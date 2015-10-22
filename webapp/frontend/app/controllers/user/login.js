import Ember from "ember";

var LoginController = Ember.Controller.extend({
  loginFailed: false,
  isProcessing: true,
  serverError: false,

actions : {
  login: function() {
  var _this = this;

    this.setProperties({
      loginFailed: false,
      isProcessing: true
    });

    var token = this.get("token");

    //var data = this.store.adapterFor('login').get('headers'),
    var host = this.store.adapterFor('login').get('host'),
    namespace = this.store.adapterFor('login').namespace,
    postUrl = [ host, namespace ].join('/'),
    headers = {'Authorization': "Token " + token};


    Ember.$.ajax({
      url: postUrl,
      headers: headers,
      crossDomain: true,
      method: 'GET',
      dataType: 'json',
      xhrFields: {withCredentials: true},
      success: function(){
          _this.set("isProcessing", false);
          _this.set("loginFailed", false);
          _this.set("serverError", false);

          _this.store.createRecord('user', {
              token: token,
              id: 1,
          });

          _this.transitionToRoute('user.clusters');
      },
      statusCode: {
        401: function() {
            _this.set("isProcessing", false);
            _this.set("loginFailed", true);
            _this.set("serverError", false);
        }
      },
      error: function() {
          _this.set("isProcessing", false);
          _this.set("serverError", true);
          _this.set("loginFailed", false);
      }
    });
  },
  dismiss: function(){
    Ember.$('#token').focus();
    Ember.$('#id_alert_wrongtoken > button').click();
    this.set('loginFailed', false);
    this.set("serverError", false);
  }
}

});

export var token;
export default LoginController;
