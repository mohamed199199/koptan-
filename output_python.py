<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تحويل الصوت RVC/So-VITS-SVC</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#5D5CDE',
                    }
                }
            },
            darkMode: 'class',
        }
    </script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    
</head>
<body class="bg-gray-100 dark:bg-gray-900 min-h-screen">
    <!-- Dark mode detection -->
    <script>
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.classList.add('dark');
        }
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
            if (event.matches) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        });
    </script>

    <div class="container mx-auto px-4 py-8">
        <header class="text-center mb-8">
            <h1 class="text-3xl font-bold text-primary mb-2">تحويل الصوت من بنت إلى ولد</h1>
            <p class="text-gray-600 dark:text-gray-400">RVC/So-VITS-SVC تقنية</p>
        </header>

        <div class="grid grid-cols-1 gap-8">
            <!-- Section 1: Trained Sample -->
            <div class="card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-bold mb-6 text-primary flex items-center">
                    <i class="fas fa-upload ml-2"></i>
                    <span>رفع العينة المدربة</span>
                </h2>
                
                <div class="space-y-4">
                    <div class="relative">
                        <label class="block text-gray-700 dark:text-gray-300 mb-2">رابط العينة من جوجل درايف</label>
                        <div class="flex">
                            <input type="text" id="driveLink" 
                                class="flex-1 text-base border border-gray-300 dark:border-gray-600 dark:bg-gray-700 rounded-r-lg p-3 focus:outline-none focus:ring-2 focus:ring-primary" 
                                placeholder="ادخل رابط العينة المدربة من جوجل درايف">
                            <button id="submitDriveLink" class="bg-primary text-white p-3 rounded-l-lg hover:bg-opacity-90 transition">
                                <i class="fas fa-link"></i>
                            </button>
                        </div>
                    </div>
                    
                    <div>
                        <label class="block text-gray-700 dark:text-gray-300 mb-2">أو قم بتحميل العينة من جهازك</label>
                        <input type="file" id="trainedSampleUpload" class="hide-file-input" accept=".pth,.pkl,.zip,.rar">
                        <label for="trainedSampleUpload" class="flex items-center justify-center w-full p-4 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                            <i class="fas fa-file-upload text-2xl text-primary ml-2"></i>
                            <span class="text-gray-700 dark:text-gray-300">اختر ملف العينة المدربة</span>
                        </label>
                        <div id="trainedSampleName" class="mt-2 text-gray-600 dark:text-gray-400 hidden"></div>
                    </div>
                </div>
            </div>

            <!-- Section 2: Sample to Convert -->
            <div class="card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-bold mb-6 text-primary flex items-center">
                    <i class="fas fa-music ml-2"></i>
                    <span>العينة المطلوب تحويلها</span>
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="space-y-4">
                        <button id="recordAudio" class="w-full flex items-center justify-center bg-primary text-white p-4 rounded-lg hover:bg-opacity-90 transition icon-btn">
                            <i class="fas fa-microphone text-xl ml-2"></i>
                            <span>تسجيل صوتي</span>
                        </button>
                        
                        <input type="file" id="audioSampleUpload" class="hide-file-input" accept="audio/*">
                        <label for="audioSampleUpload" class="flex items-center justify-center w-full p-4 border-2 border-primary rounded-lg cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                            <i class="fas fa-file-audio text-xl text-primary ml-2"></i>
                            <span>رفع عينة صوتية</span>
                        </label>
                        
                        <button id="selectAudioFile" class="w-full flex items-center justify-center bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-white p-4 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition icon-btn">
                            <i class="fas fa-folder-open text-xl ml-2"></i>
                            <span>تحديد ملف صوتي</span>
                        </button>
                    </div>
                    
                    <div class="space-y-4">
                        <div id="audioFileInfo" class="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg hidden">
                            <h4 class="font-bold mb-2">معلومات الملف</h4>
                            <p id="fileName" class="text-sm mb-1">اسم الملف: <span></span></p>
                            <p id="fileFormat" class="text-sm mb-1">الصيغة: <span></span></p>
                            <p id="fileSize" class="text-sm">الحجم: <span></span></p>
                        </div>
                        
                        <div id="audioControls" class="space-y-4 hidden">
                            <div class="flex justify-between items-center">
                                <button id="playOriginal" class="flex items-center justify-center bg-green-500 text-white p-3 rounded-lg hover:bg-green-600 transition icon-btn">
                                    <i class="fas fa-play ml-2"></i>
                                    <span>الاستماع قبل التحويل</span>
                                </button>
                                <div id="originalTime" class="text-xl font-mono font-bold text-primary">00:00</div>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <button id="playConverted" class="flex items-center justify-center bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition icon-btn disabled:opacity-50 disabled:cursor-not-allowed" disabled>
                                    <i class="fas fa-play ml-2"></i>
                                    <span>الاستماع بعد التحويل</span>
                                </button>
                                <div id="convertedTime" class="text-xl font-mono font-bold text-primary">00:00</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Section 3: Conversion Settings -->
            <div class="card bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
                <h2 class="text-xl font-bold mb-6 text-primary flex items-center">
                    <i class="fas fa-sliders-h ml-2"></i>
                    <span>إعدادات التحويل</span>
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="space-y-6">
                        <button id="convertToOpus" class="w-full flex items-center justify-center bg-primary text-white p-4 rounded-lg hover:bg-opacity-90 transition icon-btn disabled:opacity-50 disabled:cursor-not-allowed" disabled>
                            <i class="fas fa-exchange-alt text-xl ml-2"></i>
                            <span>تحويل إلى صيغة OPUS</span>
                        </button>
                        
                        <div>
                            <label class="block text-gray-700 dark:text-gray-300 mb-2 flex justify-between">
                                <span>درجة التحويل: <span id="conversionDegreeValue">15</span></span>
                            </label>
                            <input type="range" id="conversionDegree" min="1" max="30" value="15" 
                                class="w-full h-2 bg-gray-300 dark:bg-gray-700 rounded-full appearance-none cursor-pointer">
                        </div>
                        
                        <div id="conversionProgress" class="hidden">
                            <label class="block text-gray-700 dark:text-gray-300 mb-2 flex justify-between">
                                <span>تقدم التحويل</span>
                                <span id="progressPercentage">0%</span>
                            </label>
                            <div class="w-full bg-gray-300 dark:bg-gray-700 rounded-full h-4 overflow-hidden">
                                <div id="progressBar" class="h-full bg-primary transition-all duration-300" style="width: 0%"></div>
                            </div>
                            <p id="remainingTime" class="text-sm text-gray-600 dark:text-gray-400 mt-1 text-center">الوقت المتبقي: --:--</p>
                        </div>
                    </div>
                    
                    <div id="conversionActions" class="space-y-4 opacity-50 pointer-events-none">
                        <button id="downloadConverted" class="w-full flex items-center justify-center bg-green-500 text-white p-4 rounded-lg hover:bg-green-600 transition icon-btn">
                            <i class="fas fa-download text-xl ml-2"></i>
                            <span>تحميل العينة المحولة</span>
                        </button>
                        
                        <button id="shareConverted" class="w-full flex items-center justify-center bg-blue-500 text-white p-4 rounded-lg hover:bg-blue-600 transition icon-btn">
                            <i class="fas fa-share-alt text-xl ml-2"></i>
                            <span>مشاركة العينة المحولة</span>
                        </button>
                        
                        <button id="saveConverted" class="w-full flex items-center justify-center bg-purple-500 text-white p-4 rounded-lg hover:bg-purple-600 transition icon-btn">
                            <i class="fas fa-save text-xl ml-2"></i>
                            <span>حفظ العينة في موقع محدد</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // DOM Elements
        const trainedSampleUpload = document.getElementById('trainedSampleUpload');
        const trainedSampleName = document.getElementById('trainedSampleName');
        const audioSampleUpload = document.getElementById('audioSampleUpload');
        const recordAudioBtn = document.getElementById('recordAudio');
        const selectAudioFileBtn = document.getElementById('selectAudioFile');
        const audioFileInfo = document.getElementById('audioFileInfo');
        const fileName = document.getElementById('fileName').querySelector('span');
        const fileFormat = document.getElementById('fileFormat').querySelector('span');
        const fileSize = document.getElementById('fileSize').querySelector('span');
        const audioControls = document.getElementById('audioControls');
        const playOriginalBtn = document.getElementById('playOriginal');
        const playConvertedBtn = document.getElementById('playConverted');
        const originalTime = document.getElementById('originalTime');
        const convertedTime = document.getElementById('convertedTime');
        const convertToOpusBtn = document.getElementById('convertToOpus');
        const conversionDegree = document.getElementById('conversionDegree');
        const conversionDegreeValue = document.getElementById('conversionDegreeValue');
        const conversionProgress = document.getElementById('conversionProgress');
        const progressBar = document.getElementById('progressBar');
        const progressPercentage = document.getElementById('progressPercentage');
        const remainingTime = document.getElementById('remainingTime');
        const conversionActions = document.getElementById('conversionActions');
        const downloadConvertedBtn = document.getElementById('downloadConverted');
        const shareConvertedBtn = document.getElementById('shareConverted');
        const saveConvertedBtn = document.getElementById('saveConverted');
        const driveLinkInput = document.getElementById('driveLink');
        const submitDriveLink = document.getElementById('submitDriveLink');
        
        // Variables
        let originalAudio = null;
        let convertedAudio = null;
        let mediaRecorder = null;
        let recordedChunks = [];
        let isRecording = false;
        let trainedSampleFile = null;
        let conversionSimulation = null;
        let originalAudioElement = new Audio();
        let convertedAudioElement = new Audio();
        
        // GPU Acceleration settings
        const gpuAcceleration = {
            enabled: true,
            useHalfPrecision: true,
            useAMP: true,
            useONNX: false, // Will be set based on browser compatibility
            sampleRate: 24000, // 24kHz for OPUS output
            formantShiftFactor: 0.8, // Default formant shift
            pitchShiftSteps: 3, // Default pitch shift (steps)
            enhancementLevel: 0.5, // Voice enhancement level
            noiseReduction: true,
            dynamicCompression: true
        };
        
        // Check for WebGL support as a proxy for GPU capability
        function checkGPUSupport() {
            try {
                const canvas = document.createElement('canvas');
                const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
                gpuAcceleration.useONNX = !!gl;
                return !!gl;
            } catch (e) {
                gpuAcceleration.useONNX = false;
                return false;
            }
        }
        
        // Voice processing modules simulation
        const voiceProcessing = {
            hubert: {
                extract(audioData) {
                    // Simulate HuBERT feature extraction
                    console.log("Extracting voice features with HuBERT...");
                    return { features: "extracted_features", success: true };
                }
            },
            
            rvc: {
                convert(features, settings) {
                    // Simulate RVC conversion with GPU acceleration
                    console.log("Converting with RVC using settings:", settings);
                    return { success: true };
                }
            },
            
            pitchShift(audio, steps) {
                // Simulate pitch shifting
                console.log(`Pitch shifting by ${steps} steps`);
                return { success: true };
            },
            
            formantShift(audio, factor) {
                // Simulate formant shifting
                console.log(`Formant shifting by factor ${factor}`);
                return { success: true };
            },
            
            noiseReduce(audio) {
                // Simulate noise reduction
                console.log("Applying noise reduction");
                return { success: true };
            },
            
            compress(audio) {
                // Simulate dynamic range compression
                console.log("Applying dynamic compression");
                return { success: true };
            },
            
            normalize(audio) {
                // Simulate loudness normalization
                console.log("Normalizing loudness");
                return { success: true };
            },
            
            enhance(audio, level) {
                // Simulate voice enhancement
                console.log(`Enhancing voice (level: ${level})`);
                return { success: true };
            },
            
            convertToOpus(audio, sampleRate) {
                // Simulate conversion to OPUS at specific sample rate
                console.log(`Converting to OPUS format (${sampleRate}Hz)`);
                return { 
                    data: new Uint8Array(10000), // Dummy data
                    success: true 
                };
            }
        };
        
        // Event Listeners
        trainedSampleUpload.addEventListener('change', handleTrainedSampleUpload);
        audioSampleUpload.addEventListener('change', handleAudioSampleUpload);
        recordAudioBtn.addEventListener('click', toggleRecording);
        selectAudioFileBtn.addEventListener('click', simulateFileSelect);
        playOriginalBtn.addEventListener('click', togglePlayOriginal);
        playConvertedBtn.addEventListener('click', togglePlayConverted);
        convertToOpusBtn.addEventListener('click', startConversion);
        conversionDegree.addEventListener('input', updateConversionDegree);
        downloadConvertedBtn.addEventListener('click', downloadConverted);
        shareConvertedBtn.addEventListener('click', shareConverted);
        saveConvertedBtn.addEventListener('click', saveConverted);
        submitDriveLink.addEventListener('click', handleDriveLink);
        
        // Check GPU support on load
        window.addEventListener('load', () => {
            const hasGPU = checkGPUSupport();
            console.log(`GPU acceleration ${hasGPU ? 'enabled' : 'disabled'}`);
        });
        
        // Functions
        function handleTrainedSampleUpload(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            trainedSampleFile = file;
            trainedSampleName.textContent = `تم اختيار: ${file.name}`;
            trainedSampleName.classList.remove('hidden');
            
            // Enable conversion button if both samples are ready
            checkEnableConversion();
        }
        
        function handleAudioSampleUpload(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            originalAudio = file;
            displayFileInfo(file);
            createAudioPreview(file);
            
            // Enable conversion button if both samples are ready
            checkEnableConversion();
        }
        
        function handleDriveLink() {
            const link = driveLinkInput.value.trim();
            if (!link) {
                alert('الرجاء إدخال رابط صحيح');
                return;
            }
            
            // Simulate successful link submission
            trainedSampleName.textContent = `تم اختيار: ملف من جوجل درايف`;
            trainedSampleName.classList.remove('hidden');
            trainedSampleFile = { name: 'google-drive-sample.pth', size: '250MB' };
            
            // Enable conversion button if both samples are ready
            checkEnableConversion();
        }
        
        function displayFileInfo(file) {
            fileName.textContent = file.name;
            fileFormat.textContent = file.type || getExtension(file.name);
            fileSize.textContent = formatFileSize(file.size);
            audioFileInfo.classList.remove('hidden');
            audioControls.classList.remove('hidden');
        }
        
        function createAudioPreview(file) {
            const url = URL.createObjectURL(file);
            originalAudioElement.src = url;
            originalAudioElement.addEventListener('loadedmetadata', () => {
                originalTime.textContent = formatTime(originalAudioElement.duration);
            });
            
            // Cleanup previous URLs
            originalAudioElement.onload = () => {
                URL.revokeObjectURL(url);
            };
        }
        
        function toggleRecording() {
            if (isRecording) {
                stopRecording();
                recordAudioBtn.innerHTML = '<i class="fas fa-microphone text-xl ml-2"></i><span>تسجيل صوتي</span>';
                recordAudioBtn.classList.remove('bg-red-500', 'hover:bg-red-600');
                recordAudioBtn.classList.add('bg-primary', 'hover:bg-opacity-90');
            } else {
                startRecording();
                recordAudioBtn.innerHTML = '<i class="fas fa-stop-circle text-xl ml-2"></i><span>إيقاف التسجيل</span>';
                recordAudioBtn.classList.remove('bg-primary', 'hover:bg-opacity-90');
                recordAudioBtn.classList.add('bg-red-500', 'hover:bg-red-600');
            }
            isRecording = !isRecording;
        }
        
        async function startRecording() {
            recordedChunks = [];
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                mediaRecorder = new MediaRecorder(stream);
                
                mediaRecorder.addEventListener('dataavailable', e => {
                    if (e.data.size > 0) recordedChunks.push(e.data);
                });
                
                mediaRecorder.addEventListener('stop', () => {
                    const audioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
                    const file = new File([audioBlob], 'recorded-audio.webm', { type: 'audio/webm' });
                    originalAudio = file;
                    displayFileInfo(file);
                    createAudioPreview(file);
                    
                    // Enable conversion button if both samples are ready
                    checkEnableConversion();
                    
                    // Stop all tracks to release the microphone
                    stream.getTracks().forEach(track => track.stop());
                });
                
                mediaRecorder.start();
            } catch (err) {
                console.error('Error accessing microphone:', err);
                isRecording = false;
                recordAudioBtn.innerHTML = '<i class="fas fa-microphone text-xl ml-2"></i><span>تسجيل صوتي</span>';
                recordAudioBtn.classList.remove('bg-red-500', 'hover:bg-red-600');
                recordAudioBtn.classList.add('bg-primary', 'hover:bg-opacity-90');
                alert('لا يمكن الوصول إلى الميكروفون. الرجاء التحقق من صلاحيات الميكروفون في المتصفح.');
            }
        }
        
        function stopRecording() {
            if (mediaRecorder && mediaRecorder.state !== 'inactive') {
                mediaRecorder.stop();
            }
        }
        
        function simulateFileSelect() {
            // This is a demo function to simulate file selection when using selectAudioFileBtn
            const demoFile = new File([new ArrayBuffer(10000)], 'example-audio.mp3', { type: 'audio/mpeg' });
            originalAudio = demoFile;
            displayFileInfo(demoFile);
            
            // Create a dummy audio duration
            originalTime.textContent = '01:45';
            audioControls.classList.remove('hidden');
            
            // Enable conversion button if both samples are ready
            checkEnableConversion();
        }
        
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
            }
        }
        
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
            }
        }
        
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
        }
        
        function checkEnableConversion() {
            if (originalAudio && (trainedSampleFile || driveLinkInput.value.trim())) {
                convertToOpusBtn.disabled = false;
            } else {
                convertToOpusBtn.disabled = true;
            }
        }
        
        function startConversion() {
            // Disable conversion button and show progress
            convertToOpusBtn.disabled = true;
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
            console.log("Starting conversion with settings:", {
                useGPU: gpuAcceleration.enabled,
                halfPrecision: gpuAcceleration.useHalfPrecision,
                useAMP: gpuAcceleration.useAMP,
                useONNX: gpuAcceleration.useONNX,
                sampleRate: gpuAcceleration.sampleRate,
                pitchShift: gpuAcceleration.pitchShiftSteps,
                formantShift: gpuAcceleration.formantShiftFactor,
                enhancementLevel: gpuAcceleration.enhancementLevel,
                noiseReduction: gpuAcceleration.noiseReduction,
                compression: gpuAcceleration.dynamicCompression
            });
            
            // Simulate the voice conversion pipeline
            setTimeout(() => {
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
                }
                
                progressBar.style.width = `${progress}%`;
                progressPercentage.textContent = `${Math.round(progress)}%`;
                
                // Calculate remaining time
                if (progress < 100) {
                    const secondsRemaining = Math.ceil((100 - progress) * totalSeconds / 100);
                    remainingTime.textContent = `الوقت المتبقي: ${formatTime(secondsRemaining)}`;
                }
            }, intervalTime);
        }
        
        function conversionComplete() {
            // Create a dummy converted audio file with OPUS type
            convertedAudio = new File([new ArrayBuffer(10000)], 'converted-voice.opus', { type: 'audio/opus' });
            
            // Update the UI
            remainingTime.textContent = 'اكتمل التحويل!';
            
            // Enable converted audio player and action buttons
            playConvertedBtn.disabled = false;
            conversionActions.classList.remove('opacity-50', 'pointer-events-none');
            
            // Create audio preview for converted audio
            const url = URL.createObjectURL(new Blob([convertedAudio], { type: 'audio/opus' }));
            convertedAudioElement.src = url;
            convertedTime.textContent = originalTime.textContent; // Same duration as original
            
            // Cleanup
            convertedAudioElement.onload = () => {
                URL.revokeObjectURL(url);
            };
        }
        
        function downloadConverted() {
            if (!convertedAudio) return;
            
            const url = URL.createObjectURL(new Blob([convertedAudio], { type: 'audio/opus' }));
            const a = document.createElement('a');
            a.href = url;
            a.download = 'converted-voice.opus';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }
        
        function shareConverted() {
            if (!convertedAudio) return;
            
            // Check if Web Share API is available
            if (navigator.share) {
                // Create a file object from the converted audio
                const file = new File([convertedAudio], 'converted-voice.opus', { type: 'audio/opus' });
                
                // Share the file
                navigator.share({
                    title: 'العينة الصوتية المحولة',
                    files: [file]
                }).catch(err => {
                    console.error('Error sharing:', err);
                    
                    // Fallback for sharing on mobile apps
                    shareViaIntent();
                });
            } else {
                // Try fallback methods for sharing
                shareViaIntent();
            }
        }
        
        function shareViaIntent() {
            // Fallback method for sharing on mobile
            // Create a temporary link for the file
            const url = URL.createObjectURL(new Blob([convertedAudio], { type: 'audio/opus' }));
            
            // Create intent URL for common messaging apps
            const intentUrls = {
                whatsapp: `whatsapp://send?text=العينة الصوتية المحولة ${encodeURIComponent(url)}`,
                telegram: `tg://msg?text=العينة الصوتية المحولة ${encodeURIComponent(url)}`,
                facebook: `fb-messenger://share/?link=${encodeURIComponent(url)}`
            };
            
            // Create sharing options
            const shareDiv = document.createElement('div');
            shareDiv.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
            shareDiv.innerHTML = `
                <div class="bg-white dark:bg-gray-800 p-6 rounded-xl max-w-sm mx-auto">
                    <h3 class="text-lg font-bold mb-4 text-gray-800 dark:text-white">مشاركة العينة الصوتية</h3>
                    <div class="grid grid-cols-3 gap-4 mb-4">
                        <button class="whatsapp flex flex-col items-center p-3 rounded-lg bg-green-100 hover:bg-green-200">
                            <i class="fab fa-whatsapp text-2xl text-green-600 mb-1"></i>
                            <span class="text-sm">واتساب</span>
                        </button>
                        <button class="telegram flex flex-col items-center p-3 rounded-lg bg-blue-100 hover:bg-blue-200">
                            <i class="fab fa-telegram text-2xl text-blue-600 mb-1"></i>
                            <span class="text-sm">تليجرام</span>
                        </button>
                        <button class="messenger flex flex-col items-center p-3 rounded-lg bg-indigo-100 hover:bg-indigo-200">
                            <i class="fab fa-facebook-messenger text-2xl text-indigo-600 mb-1"></i>
                            <span class="text-sm">ماسنجر</span>
                        </button>
                    </div>
                    <button class="cancel w-full py-2 bg-gray-200 hover:bg-gray-300 rounded-lg text-gray-800">إلغاء</button>
                </div>
            `;
            
            document.body.appendChild(shareDiv);
            
            // Add event listeners to buttons
            shareDiv.querySelector('.whatsapp').addEventListener('click', () => {
                window.location.href = intentUrls.whatsapp;
                document.body.removeChild(shareDiv);
            });
            
            shareDiv.querySelector('.telegram').addEventListener('click', () => {
                window.location.href = intentUrls.telegram;
                document.body.removeChild(shareDiv);
            });
            
            shareDiv.querySelector('.messenger').addEventListener('click', () => {
                window.location.href = intentUrls.facebook;
                document.body.removeChild(shareDiv);
            });
            
            shareDiv.querySelector('.cancel').addEventListener('click', () => {
                document.body.removeChild(shareDiv);
            });
            
            // Clean up the temporary URL
            setTimeout(() => {
                URL.revokeObjectURL(url);
            }, 60000); // Revoke after 1 minute
        }
        
        function saveConverted() {
            if (!convertedAudio) return;
            
            try {
                // For browsers that support the File System Access API
                if ('showSaveFilePicker' in window) {
                    (async () => {
                        try {
                            const handle = await window.showSaveFilePicker({
                                suggestedName: 'converted-voice.opus',
                                types: [{
                                    description: 'OPUS Audio File',
                                    accept: { 'audio/opus': ['.opus'] }
                                }]
                            });
                            
                            const writable = await handle.createWritable();
                            await writable.write(convertedAudio);
                            await writable.close();
                        } catch (err) {
                            if (err.name !== 'AbortError') {
                                console.error('Failed to save file:', err);
                                // Fall back to regular download
                                downloadConverted();
                            }
                        }
                    })();
                } else {
                    // Fall back to regular download for browsers without File System Access API
                    downloadConverted();
                }
            } catch (err) {
                console.error('Error in save function:', err);
                // Final fallback
                downloadConverted();
            }
        }
        
        // Helper functions
        function formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }
        
        function formatTime(seconds) {
            seconds = Math.round(seconds);
            const minutes = Math.floor(seconds / 60);
            seconds = seconds % 60;
            return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        }
        
        function getExtension(filename) {
            return filename.split('.').pop().toUpperCase();
        }
    </script>
</body>
</html>