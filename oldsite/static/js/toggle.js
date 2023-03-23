const currentPagePath = window.location.pathname;
const currentPageName = currentPagePath.substring(currentPagePath.lastIndexOf('/') + 1);

const pageToggle = document.getElementById('page-toggle');

pageToggle.addEventListener('click', function() {
  window.location.href = '../' + currentPageName;
});
