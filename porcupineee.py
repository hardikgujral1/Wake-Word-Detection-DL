import struct
import pvporcupine
import pyaudio

def main():
    # Path to the Porcupine library file for your platform
    # library_path = "path/to/your/porcupine/library"

    # Path to the Porcupine keyword file for your custom wake word "Friday"
    # keyword_paths = [' jarvis']

    # Create an instance of the Porcupine engine
    handle = pvporcupine.create(keyword_paths=["E:\Projects\Friday 2.0\Friday_en_windows_v3_0_0.ppn"],access_key="tXDEotkcuTDxqF/P6DOjbHH1R7iq7Ftq88hiiMB/T+nt8KTZyBcj8Q==",sensitivities=[1])

    try:
        # Create an instance of PyAudio
        p = pyaudio.PyAudio()

        # Open a stream with the input device
        stream = p.open(
            rate=handle.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=handle.frame_length  # Ensure this matches Porcupine's frame length
        )

        print("Listening for the wake word. Press Ctrl+C to exit.")

        while True:
            # Read a single frame from the audio stream
            pcm = stream.read(handle.frame_length)
            pcm=struct.unpack_from("h"*handle.frame_length,pcm)
            # Process the frame with Porcupine
            keyword_index=handle.process(pcm)
            # # result = handle.process(pcm)
            if keyword_index>=0:
                print("Hotword Detected")
            
                
            # # Check if the wake word was detected
            # if result:
            #     print("Wake word detected!")

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        # Release resources
        handle.delete()
        stream.close()
        p.terminate()
        print("terminated")

if __name__ == "__main__":
    main()
