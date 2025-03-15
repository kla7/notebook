let edited = document.querySelector('edited');
let hover = document.querySelector('hover');

edited.addEventListener('mouseover', () => {
    hover.style.visibility = 'visible';
});

edited.addEventListener('mouseout', () => {
    hover.style.visibility = 'hidden';
});