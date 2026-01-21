async function removeBg() {
    const input = document.getElementById("imageInput");
    const file = input.files[0];
    const loader = document.getElementById("loader");
    const result = document.getElementById("result");
    const download = document.getElementById("download");

    if (!file) {
        alert("Please select an image");
        return;
    }

    loader.style.display = "block";
    download.style.display = "none";
    result.src = "";

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/remove-bg", {
        method: "POST",
        body: formData
    });

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);

    loader.style.display = "none";
    result.src = url;
    download.href = url;
    download.style.display = "inline-block";
}
