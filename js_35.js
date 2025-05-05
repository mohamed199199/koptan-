        function formatTime(seconds) {
            seconds = Math.round(seconds);
            const minutes = Math.floor(seconds / 60);
            seconds = seconds % 60;