const currentPagePath = window.location.pathname;
const currentPageName = currentPagePath.substring(currentPagePath.lastIndexOf('/') + 1);

const pageToggle = document.getElementById('page-toggle');

if (pageToggle.hasAttribute('data-target')) {
  const redirectPageName = pageToggle.getAttribute('data-target');
  pageToggle.addEventListener('click', function() {
    window.location.href = './oldsite/' + redirectPageName;
  });
} else {
  pageToggle.addEventListener('click', function() {
    window.location.href = './oldsite/' + currentPageName;
  });
};
