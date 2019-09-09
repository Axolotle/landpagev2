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
