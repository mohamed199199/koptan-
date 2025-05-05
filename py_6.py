                recordAudioBtn.classList.remove('bg-red-500', 'hover:bg-red-600');
                recordAudioBtn.classList.add('bg-primary', 'hover:bg-opacity-90');
            } else {
                startRecording();
                recordAudioBtn.innerHTML = '<i class="fas fa-stop-circle text-xl ml-2"></i><span>إيقاف التسجيل</span>';
                recordAudioBtn.classList.remove('bg-primary', 'hover:bg-opacity-90');
                recordAudioBtn.classList.add('bg-red-500', 'hover:bg-red-600');