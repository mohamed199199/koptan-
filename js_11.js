        function handleAudioSampleUpload(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            originalAudio = file;
            displayFileInfo(file);
            createAudioPreview(file);
            
            // Enable conversion button if both samples are ready
            checkEnableConversion();