import Ember from 'ember';
import ENV from 'frontend/config/environment';

var Router = Ember.Router.extend({
  location: ENV.locationType,
});

Router.map(function() {

  //user routes
  this.resource('user', function() {
		// /user/login
		this.route('login');
  		// /user/logout
  		this.route('logout');
    // /user/clusters
    this.route('clusters');
	});

  //apps routes
  this.resource('apps', function() {
    // /apps/upload
    this.route('upload');
  });
});

export default Router;
