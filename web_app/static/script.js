/*Abre e fecha menu lateral  em modo mobile*/
const menuMobile = document.querySelector('.menu-mobile')
const body = document.querySelector('body')

menuMobile.addEventListener('click', () =>{
    /*Condição ternario*/ 
    menuMobile.classList.contains("bi-list-ul") ? menuMobile.classList.replace("bi-list-ul", "bi-x"): 
    /*Adicionando nova class no body*/
    menuMobile.classList.replace("bi-x", "bi-list-ul");
    body.classList.toggle("menu-nav-active");
} );


/* Fecha o menu quando clicar em algum item e muda o icone para list */
const navItem = document.querySelectorAll(".nav-item")
navItem.forEach(item => {
    item.addEventListener("click", () =>{
    if (body.classList.contains("menu-nav-active")) 
    body.classList.remove("menu-nav-active")
    menuMobile.classList.replace("bi-x", "bi-list-ul")
})})

// Animar todos os itens na tela que tiverem meu atributo data-anime
const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
  const windowTop = window.pageYOffset + window.innerHeight * 0.85 ;

  item.forEach((element) => {
    if (windowTop > element.offsetTop) {
      element.classList.add("animate");
    } else {
      element.classList.remove("animate");
    }
  });
};

animeScroll();

window.addEventListener("scroll", ()=>{
  animeScroll();
})

// Ativar carregamento no botão de enviar formulário para

const btnEnviar = document.querySelector('#btn-enviar')
const btnEnviarLoader = document.querySelector('#btn-enviar-loader')
const nome = document.querySelector('#nome').value()
const email = document.querySelector('#email').value()
const mensagem = document.querySelector('#mensagem').value()

btnEnviar.addEventListener("click", ()=>{
  btnEnviarLoader.style.display = "block";
  btnEnviar.style.display = "none"
})

// Tira a mensagem de sucesso depois de 5 segundos

setTimeout(() => {

  if (nome != null && email != null && mensagem != null){
    document.querySelector('#alerta').style.display = 'none';
  }

}, 5000)