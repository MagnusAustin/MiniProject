// Elements
const dropZone = document.querySelector("#drop-zone");
const fileInput = document.querySelector("#file-upload");
const progressBar = document.querySelector("#progress-bar");
const fileList = document.querySelector("#file-list");
const submitButton = document.querySelector("#submit-button");
const resultsSection = document.querySelector("#results-section");
const resultsSummary = document.querySelector("#results-summary");
const resultsTable = document.querySelector("#results-table");

// Event Listeners
dropZone.addEventListener("dragover", handleDragOver);
dropZone.addEventListener("dragleave", handleDragLeave);
dropZone.addEventListener("drop", handleDrop);
fileInput.addEventListener("change", handleFileSelect);
submitButton.addEventListener("click", handleSubmit);

// Drag & Drop Handlers
function handleDragOver(event) {
    event.stopPropagation();
    event.preventDefault();
    event.dataTransfer.dropEffect = "copy";
    dropZone.classList.add("drag-over");
}

function handleDragLeave(event) {
    event.stopPropagation();
    event.preventDefault();
    dropZone.classList.remove("drag-over");
}

function handleDrop(event) {
    event.stopPropagation();
    event.preventDefault();
    dropZone.classList.remove("drag-over");

    const files = event.dataTransfer.files;
    handleFiles(files);
}

// File Input Handler
function handleFileSelect(event) {
    const files = event.target.files;
    handleFiles(files);
}

// File Handling Functions
function handleFiles(files) {
    fileList.innerHTML = "";
    resultsSection.style.display = "none";

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const listItem = document.createElement("li");
        listItem.textContent = `${file.name} (${formatFileSize(file.size)})`;
        fileList.appendChild(listItem);
    }
}

function formatFileSize(size) {
    if (size >= 1000000) {
        return `${(size / 1000000).toFixed(2)} MB`;} 
    else if (size >= 1000) {
        return `${(size / 1000).toFixed(2)} KB`;}
    else {
        return `${size} bytes`;
        }
        }
