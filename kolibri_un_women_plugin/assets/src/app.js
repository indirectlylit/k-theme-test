import RootVue from './views';


import KolibriApp from 'kolibri_app';
import { initialState, mutations } from './state/store';

const routes = [];

class UnWomenPluginModule extends KolibriApp {
  get stateSetters() {
    return [];
  }
  get routes() {
    return routes;
  }
  get RootVue() {
    return RootVue;
  }
  get initialState() {
    return initialState;
  }
  get mutations() {
    return mutations;
  }
}



const unWomenPlugin = new UnWomenPluginModule();

export { unWomenPlugin as default };
