function funcThisSize() {
    $("#innerWidth").html( window.innerWidth );
    $("#innerHeight").html( window.innerHeight );
    $("#outerWidth").html( window.outerWidth );
    $("#outerHeight").html( window.outerHeight );
}

$(function(){
    $(window).resize( funcThisSize );
    funcThisSize();
});

var Body={
  setBackgroundColor:function(color){
    $('body').css("background-color",color);
  }
}
var Links={
  setColor:function(color){
    // var alist=document.querySelectorAll('a');
    // for (var i=0; i<alist.length; i++) {
    //   alist[i].style.color=color;
    $('a').css("color",color);
    }
  }

function ntd(self){
  if(self.value === 'night'){
    Body.setBackgroundColor('black');
    self.value = 'day';
    Links.setColor('powderblue');
} else {
    Body.setBackgroundColor('white');
    self.value = 'night';
    Links.setColor('blue');
  }
}
