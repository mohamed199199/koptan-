        function saveConverted() {
            if (!convertedAudio) return;
            
            try {
                // For browsers that support the File System Access API
                if ('showSaveFilePicker' in window) {
                    (async () => {
                        try {
                            const handle = await window.showSaveFilePicker({