        function displayFileInfo(file) {
            fileName.textContent = file.name;
            fileFormat.textContent = file.type || getExtension(file.name);
            fileSize.textContent = formatFileSize(file.size);