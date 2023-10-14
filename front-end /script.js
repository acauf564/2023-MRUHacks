const affirmations = [
    "I am healthy",
    "I am intelligent",
    "I am confident",
    "I am successful",
    "I am happy",
];

const affirmationElement = document.querySelector('.affirmation');

function displayNextAffirmation() {
    const currentAffirmation = affirmationElement.textContent;
    const currentIndex = affirmations.indexOf(currentAffirmation);
    const nextIndex = (currentIndex + 1) % affirmations.length;
    affirmationElement.textContent = affirmations[nextIndex];
}

setInterval(displayNextAffirmation, 7000);

displayNextAffirmation();

const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileInput");
const fileList = document.getElementById("file-list");

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("drag-over");
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("drag-over");
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("drag-over");

    const files = e.dataTransfer.files;
    handleFiles(files);
});

fileInput.addEventListener("change", (e) => {
    const files = e.target.files;
    handleFiles(files);
});

function handleFiles(files) {
    for (const file of files) {
        const listItem = document.createElement("li");
        listItem.textContent = file.name;
        fileList.appendChild(listItem);
    }
}

