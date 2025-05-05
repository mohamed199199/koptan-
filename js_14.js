        function createAudioPreview(file) {
            const url = URL.createObjectURL(file);
            originalAudioElement.src = url;
            originalAudioElement.addEventListener('loadedmetadata', () => {
                originalTime.textContent = formatTime(originalAudioElement.duration);
            });
            
            // Cleanup previous URLs
            originalAudioElement.onload = () => {
                URL.revokeObjectURL(url);
            };