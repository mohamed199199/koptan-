        function shareConverted() {
            if (!convertedAudio) return;
            
            // Check if Web Share API is available
            if (navigator.share) {
                // Create a file object from the converted audio