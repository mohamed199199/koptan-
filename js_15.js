        function toggleRecording() {
            if (isRecording) {
                stopRecording();
                recordAudioBtn.innerHTML = '<i class="fas fa-microphone text-xl ml-2"></i><span>تسجيل صوتي</span>';