import DS from "ember-data";
import ENV from 'frontend/config/environment';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';

export default DS.JSONAPIAdapter.extend({
  host: ENV.host + ':80',
  namespace: 'api',
 });
