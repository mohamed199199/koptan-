        // Functions
        function handleTrainedSampleUpload(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            trainedSampleFile = file;