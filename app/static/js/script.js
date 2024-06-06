

// function selectFolder() {
//     const folderInput = document.getElementById('folderInput');
//     folderInput.click();
// }

// function checkImage() {
//     const fileInput = document.getElementById('fileInput');
//     fileInput.click();
// }

// document.getElementById('folderInput').addEventListener('change', function(event) {
//     const files = event.target.files;
//     if (files.length > 0) {
// // Extract the folder path from the first file's webkitRelativePath
//         const folderPath = files[0].webkitRelativePath.split('/')[0];
//         // const folderPath = fullPath.substring(0, fullPath.lastIndexOf('/'));
//         // const folderPath = files[0].webkitRelativePath.split('/')[0];
//         document.getElementById('paths-list').innerHTML += `
//         <div class="p-2 d-flex align-items-center path" onclick="toggleCheckbox(this)">
//             <input type="checkbox" class="form-checkbox" />
//             <div>${folderPath}</div>
//         </div>
//         `;
//     }
// });

// document.getElementById('fileInput').addEventListener('change', function(event) {
//     const file = event.target.files[0];
//     if (file) {
//         if (file.type.startsWith('image/')) {
//             const imageContainer = document.getElementById('image-container');
//             imageContainer.innerHTML = `<img src="${URL.createObjectURL(file)}" alt="Selected Image" style="max-width: 100%;">`;
//         } else {
//             alert("The selected file is not an image.");
//         }
//     }
// });

document.addEventListener('DOMContentLoaded', function() {
    var currentYear = new Date().getFullYear();
    document.getElementById('currentYear').textContent = currentYear;
});

function toggleCheckbox(element) {
    const checkbox = element.querySelector('input[type="checkbox"]');
    checkbox.checked = !checkbox.checked;
}
