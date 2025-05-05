        function updateConversionDegree() {
            conversionDegreeValue.textContent = conversionDegree.value;
            
            // Update conversion settings based on slider value
            const value = parseInt(conversionDegree.value);
            
            // Calculate normalized values between 0-1 based on slider position
            const normalizedValue = (value - 1) / 29; // 1-30 range normalized to 0-1
            
            // Update settings based on slider
            gpuAcceleration.pitchShiftSteps = Math.round(normalizedValue * 12 - 6); // -6 to +6 semitones
            gpuAcceleration.formantShiftFactor = 0.7 + normalizedValue * 0.6; // 0.7 to 1.3
            gpuAcceleration.enhancementLevel = 0.3 + normalizedValue * 0.7; // 0.3 to 1.0