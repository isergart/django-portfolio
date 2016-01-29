function setEqualHeight(columns) {
 var tallestcolumn = 0;
  columns.each( function() {
   currentHeight = $(this).height();
    if(currentHeight > tallestcolumn) {
     tallestcolumn = currentHeight;
 } });
  columns.height(tallestcolumn);
   }
$(document).ready(function() {
    setEqualHeight($(".container > div"));
});
//*******
// $(document).ready(function() {
//   setTimeout(function() {
//       var mainDivs = $(".column"); //Получаем все элементы с классом column
//       var maxHeight = 0;
//       for (var i = 0; i < mainDivs.length; ++i) {
//         if (maxHeight < $(mainDivs[i]).height()) { //Находим максимальную высоту
//           maxHeight = $(mainDivs[i]).height();
//         }
//       }
//       for (var i = 0; i < mainDivs.length; ++i) {
//         $(mainDivs[i]).height(maxHeight); //Устанавливаем всем элементам максимальную высоту
//       }
//     }, 0);
// });
//*******
// window.onload = function() {
//   setTimeout(function() {
//       var mainDivs = document.getElementsByClassName("column");
//       var maxHeight = 0;
//       for (var i = 0; i < mainDivs.length; ++i) {
//         if (maxHeight < mainDivs[i].clientHeight) {
//           maxHeight = mainDivs[i].clientHeight;
//         }
//       }
//       for (var i = 0; i < mainDivs.length; ++i) {
//         mainDivs[i].style.height = maxHeight + "px";
//       }
//     }, 1000);
// }
//*******
// $.fn.setEqualHeight = function() {
//     $this = this;
//     setTimeout(function() {
//       var maxHeight = 0;
//       $this.each(function() {
//         if (maxHeight < $(this).height()) {
//           maxHeight = $(this).height();
//         }
//       });
//       $this.each(function() {
//         $(this).height(maxHeight);
//       });
//     }, 1000);
// }
// $(document).ready(function() {
//   $(".column").setEqualHeight();
// });
//*******
