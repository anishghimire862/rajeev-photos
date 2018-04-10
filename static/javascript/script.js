var current = 1;
function previous() {
    var images = document.getElementsByClassName('show-dialog');
    if(Number(images[current-1].getAttribute('id')) <= 1){
        current = images.length + 1;
    }
    current--;
    setImage(images);
}

function next() {
    var images = document.getElementsByClassName('show-dialog');
    if(Number(images[current-1].getAttribute('id')) >= images.length){
        current = 0;
    }
    current++;
    setImage(images);
}

function setImage(images) {
    document.querySelector(
        '#modal-image').src = images[current-1].getAttribute('data-url');
}