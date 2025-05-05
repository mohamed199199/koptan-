        function togglePlayOriginal() {
            if (originalAudioElement.paused) {
                originalAudioElement.play();
                playOriginalBtn.innerHTML = '<i class="fas fa-pause ml-2"></i><span>إيقاف</span>';
                
                // Add event to reset button when audio ends
                originalAudioElement.onended = () => {
                    playOriginalBtn.innerHTML = '<i class="fas fa-play ml-2"></i><span>الاستماع قبل التحويل</span>';
                };
            } else {
                originalAudioElement.pause();
                playOriginalBtn.innerHTML = '<i class="fas fa-play ml-2"></i><span>الاستماع قبل التحويل</span>';