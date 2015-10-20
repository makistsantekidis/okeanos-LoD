import Ember from "ember";
import SessionService from 'ember-simple-auth/services/session';

var UploadController = Ember.Controller.extend({
  sameUpload: false,
  serverError: false,
  successUpload: false,
  session: Ember.inject.service('session'),

  actions : {
    upload: function() {
    var _this = this;

      this.setProperties({
        sameUpload: false,
        serverError: false,
        successUpload: false,
      });

      var host = this.store.adapterFor('upload-app').get('host'),
      namespace = this.store.adapterFor('upload-app').namespace,
      postUrl = [ host, namespace ].join('/');
      const headers = {};

      this.get('session').authorize('authorizer:django', (headerName, headerValue) => {
      headers["Authorization"] = headerValue;
      Ember.$.ajax('/secret-data', { headers });
      });

      var data = new FormData(document.getElementById("upload-app-form"));

      Ember.$.ajax({
        url: postUrl,
        headers: headers,
        method: 'POST',
        processData: false,
        contentType: false,
        data: data,
        success: function(){
          console.log("success");
          _this.set("successUpload", true);
          _this.set("sameUpload", false);
          _this.set("serverError", false);
        },
        statusCode: {
          400: function() {
            _this.set("sameUpload", true);
            _this.set("serverError", false);
            _this.set("successUpload", false);
          }
        },
        error: function() {
          _this.set("sameUpload", false);
          _this.set("serverError", true);
          _this.set("successUpload", false);
        }
      });
    },
  },

});

export default UploadController;
