document.querySelectorAll('.selector a').forEach(selector => {
    selector.onclick = function () {
        document.querySelectorAll('#projects li').forEach(project => {
            if (!project.dataset.keywords.includes(this.dataset.keyword)) {
                project.classList.add('hide');
            } else {
                project.classList.remove('hide');
            }
        });
        document.querySelectorAll('.synopsis .container').forEach(container => {
            console.log(container);
            if (container.dataset.keyword.includes(this.dataset.keyword)) {
                container.classList.remove('hide');
            } else {
                container.classList.add('hide');
            }
        });
        document.querySelectorAll('.selector .selected').forEach(selected => {
            selected.classList.remove('selected');
        });
        this.parentElement.parentElement.classList.add('selected');
    }
});

document.querySelectorAll('.gallery button').forEach((elem, index, elems) => {
    elem.onclick = function () {
        var actual = document.querySelector('.gallery figure:not(.hide)');
        var next = this.name == 'previous' 
            ? actual.previousElementSibling
            : actual.nextElementSibling;
        actual.classList.add('hide');
        next.classList.remove('hide');
        if (next.nextElementSibling == null) elems[1].classList.add('hide');
        else elems[1].classList.remove('hide');
        if (next.previousElementSibling == null) elems[0].classList.add('hide');
        else elems[0].classList.remove('hide');            
    }
})
