        function checkEnableConversion() {
            if (originalAudio && (trainedSampleFile || driveLinkInput.value.trim())) {
                convertToOpusBtn.disabled = false;
            } else {
                convertToOpusBtn.disabled = true;