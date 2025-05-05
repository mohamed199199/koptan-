                console.error('Error accessing microphone:', err);
                isRecording = false;
                recordAudioBtn.innerHTML = '<i class="fas fa-microphone text-xl ml-2"></i><span>تسجيل صوتي</span>';