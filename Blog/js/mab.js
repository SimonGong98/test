function Bebold(self) {
  self.style='font: italic bold; text-decoration:underline;'
  var afonts=document.querySelector('a.font');
  afonts.value==='on';

  var itemsWithoutCurrent =
    items.filter(function(x) { return x !== self; });
  itemsWithoutCurrent.value==='off';
  itemsWithoutCurrent.style=
  'font: monospace bold 1rem Georgia, sans-serif;
  font-size: large; text-decoration-line: none; color: black;'
}

function fetchPage(name){
  fetch(name).then(function(response){
    response.text().then(function(text){
      document.querySelector('my-box').innerHTML = text;
    })
  });
}
