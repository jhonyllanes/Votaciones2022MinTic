import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
 
  {
    title: 'Login',
    icon: 'shopping-cart-outlin',
    link: '/pages/seguridad/login',
    home: true,
  },


  {
    title: 'Candidatos',
    icon: 'layout-outline',
    children: [
      {
        title: 'Listar',
        link: '/pages/candidatos/listar',
      },
      {
        title: 'Crear',
        link: '/pages/candidatos/crear',
      },
    
    ],
  },
  {
    title: 'Partidos',
    icon: 'layout-outline',
    children: [
      {
        title: 'Listar',
        link: '/pages/partidos/listar',
      },
      {
        title: 'Crear',
        link: '/pages/partidos/crear',
      },
     
    ],
  },
  {
    title: 'Mesas',
    icon: 'layout-outline',
    children: [
      {
        title: 'Listar',
        link: '/pages/mesas/listar',
      },
      {
        title: 'Crear',
        link: '/pages/mesas/crear',
      },
     
    ],
  },
 
    
  
];
