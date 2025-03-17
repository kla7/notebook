let edited = document.querySelector('edited');
let hover = document.querySelector('hover');

if (edited) {
    edited.addEventListener('mouseover', () => {
        hover.style.visibility = 'visible';
    });

    edited.addEventListener('mouseout', () => {
        hover.style.visibility = 'hidden';
    });
}

let collapse = document.querySelector('.collapsible');
let comments = document.querySelector('.comments')

if (collapse) {
    collapse.addEventListener('click', () => {
        if (comments.style.display === 'block') {
            comments.style.display = 'none';
        } else {
            comments.style.display = 'block';
        }
    });
}