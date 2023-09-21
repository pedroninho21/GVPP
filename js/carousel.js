// Créer un tableau d'images
var images = [];

for (var i = 0; i < data.length; i++) {
  images.push({
    id: data[i]["id"],
    marque: data[i]["marque"],
    modele: data[i]["modele"],
    url: data[i]["photo"]
  });
}

// Créer un carrousel
var carousel = document.querySelector(".carousel");

// Initialiser le carrousel
carousel.style.width = "700px";
carousel.style.height = "440px";

// Ajouter les images au carrousel
for (var i = 0; i < images.length; i++) {

  // Créer un élément <div>
  var div = document.createElement("div");
  div.className = "slide";

  // Créer un élément <img>
  var img = document.createElement("img");
  img.src = images[i].url;
  img.alt = images[i].marque + " " + images[i].modele;

  // Ajouter l'élément <img> à l'élément <div>
  div.appendChild(img);

  // Ajouter l'élément <div> au carrousel
  carousel.appendChild(div);
}

// Ajouter des boutons de navigation
var buttonLeft = document.createElement("button");
buttonLeft.className = "button left";
buttonLeft.textContent = "<";

var buttonRight = document.createElement("button");
buttonRight.className = "button right";
buttonRight.textContent = ">";

carousel.appendChild(buttonLeft);
carousel.appendChild(buttonRight);

// Écouter les événements sur les boutons
buttonLeft.addEventListener("click", function() {
  carousel.scrollLeft -= 1;
});

buttonRight.addEventListener("click", function() {
  carousel.scrollLeft += 1;
});

// Initialiser le carrousel
carousel.scrollLeft = 0;