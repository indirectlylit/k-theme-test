import theme from './styles/theme.styl';
import keenVars from './styles/keen.scss';
import logo from './views/logo';

export default {
  styles: {
    theme,
    keenVars,
  },
  coreVue: {
    components: {
      logo,
    },
  },
};
