            conversionProgress.classList.remove('hidden');
            
            // Update settings based on slider before conversion
            updateConversionDegree();
            
            // Simulate conversion process with more realistic timing
            let progress = 0;
            const totalSeconds = 25; // Simulate 25 seconds conversion
            const intervalTime = 200; // Update every 200ms
            const steps = (totalSeconds * 1000) / intervalTime;
            const increment = 100 / steps;
            
            // Clear any existing interval
            if (conversionSimulation) clearInterval(conversionSimulation);
            
            // Log conversion settings