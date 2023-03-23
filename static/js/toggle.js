const currentPagePath = window.location.pathname;
const currentPageName = currentPagePath.substring(currentPagePath.lastIndexOf('/') + 1);
console.log(currentPageName);

const pageToggle = document.getElementById('page-toggle');
let currentPage = currentPageName;

pageToggle.addEventListener('click', function() {
  window.location.href = './oldsite/' + currentPageName;
});
