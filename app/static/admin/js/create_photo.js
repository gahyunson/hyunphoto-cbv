// static/admin/js/create_photo.js
document.addEventListener("DOMContentLoaded", function () {
    const button = document.createElement('button');
    button.textContent = "Create Photo";
    button.classList.add('button', 'btn', 'btn-primary');

    button.addEventListener('click', function () {
        fetch('/admin/myapp/photos/create-photo/')
            .then(response => response.json())
            .then(data => {
                alert("Photo created successfully: " + JSON.stringify(data));
            })
            .catch(error => {
                alert("Error creating photo: " + error);
            });
    });

    // Admin 페이지에 버튼 추가
    const adminHeader = document.querySelector('.object-tools');
    if (adminHeader) {
        adminHeader.appendChild(button);
    }
});
