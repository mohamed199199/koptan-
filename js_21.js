        function togglePlayConverted() {
            if (!convertedAudio) return;
            
            if (convertedAudioElement.paused) {
                convertedAudioElement.play();
                playConvertedBtn.innerHTML = '<i class="fas fa-pause ml-2"></i><span>إيقاف</span>';
                
                // Add event to reset button when audio ends
                convertedAudioElement.onended = () => {
                    playConvertedBtn.innerHTML = '<i class="fas fa-play ml-2"></i><span>الاستماع بعد التحويل</span>';
                };
            } else {
                convertedAudioElement.pause();
                playConvertedBtn.innerHTML = '<i class="fas fa-play ml-2"></i><span>الاستماع بعد التحويل</span>';