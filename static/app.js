// destination overview page
const lists = [...document.querySelectorAll(".accordion_li")];

lists.map((li) => {
  li.addEventListener("click", () => {
    const p = li.querySelector(".accordion_hide");
    const icon = li.querySelector(".fa-solid");
    if (p.style.height && p.style.height !== "0px") {
      p.style.height = 0;
      icon.classList.remove("fa-angle-up");
      icon.classList.add("fa-angle-down");
      return; 
    }
    lists.forEach((otherLi) => {
      if (otherLi !== li) {
        const otherP = otherLi.querySelector(".accordion_hide");
        const otherIcon = otherLi.querySelector(".fa-solid");
        otherP.style.height = 0;
        otherIcon.classList.remove("fa-angle-up");
        otherIcon.classList.add("fa-angle-down");
      }
    });
    p.style.height = p.scrollHeight + "px";
    icon.classList.remove("fa-angle-down");
    icon.classList.add("fa-angle-up");
  });
});

// home page
const nav_links = document.querySelector(".nav_links ul");
const menu_btn = document.getElementById("menu_btn");

menu_btn.addEventListener("click", () =>{
  nav_links.classList.toggle("active")
})


// best holiday page
const filters = [...document.querySelectorAll(".filter_col")];

filters.map((filter) => {
  filter.addEventListener("click" , () => {
    filter.classList.toggle("open");
  });
});


const list = document.querySelector(".list");
const grid = document.querySelector(".grid");
const cards = [...document.querySelectorAll(".listing_card")];

list.addEventListener("click" , () => {
    cards.map((card) => {
        card.classList.add("list");
    });
    grid.classList.remove("active");
    list.classList.add("active");
});
grid.addEventListener("click" , () => {
    cards.map((card) => {
        card.classList.remove("list");
    });
    grid.classList.add("active");
    list.classList.remove("active");
});