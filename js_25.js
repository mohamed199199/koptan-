                console.log("Extracting audio features...");
                remainingTime.textContent = `جاري استخراج خصائص الصوت...`;
            }, 1000);
            
            setTimeout(() => {
                console.log("Running RVC model...");
                remainingTime.textContent = `جاري تطبيق نموذج RVC...`;
            }, 5000);
            
            setTimeout(() => {
                console.log("Applying pitch and formant shifting...");
                remainingTime.textContent = `جاري تعديل طبقة الصوت...`;
            }, 10000);
            
            setTimeout(() => {
                console.log("Post-processing audio...");
                remainingTime.textContent = `جاري المعالجة النهائية...`;
            }, 15000);
            
            setTimeout(() => {
                console.log("Converting to OPUS format...");
                remainingTime.textContent = `جاري التحويل إلى صيغة OPUS...`;
            }, 20000);
            
            conversionSimulation = setInterval(() => {
                progress += increment;
                if (progress >= 100) {
                    progress = 100;
                    clearInterval(conversionSimulation);
                    conversionComplete();