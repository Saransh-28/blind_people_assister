
import cv2
import numpy as np

# Initialize video capture for two cameras (0 and 1 are typical camera indices)
cap1 = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture(1)

# Check if camera streams were opened successfully
# if not cap1.isOpened() or not cap2.isOpened():
if not cap1.isOpened():
    print("Error: Could not open camera(s).")
else:
    while True:
        # Read frames from both cameras
        ret1, frame1 = cap1.read()
        # ret2, frame2 = cap2.read()
        ret2, frame2 = cap1.read()

        # Resize frames to the desired dimensions
        frame1 = cv2.resize(frame1, (400, 300), interpolation=cv2.INTER_AREA)
        frame2 = cv2.resize(frame2, (400, 300), interpolation=cv2.INTER_AREA)

        if not ret1 or not ret2:
            print("Error: Could not read frames from camera(s).")
            break

        # Get the dimensions of the frames
        height, width, _ = frame1.shape

        # Calculate the x-coordinates of the 9 equidistant vertical lines
        num_x_lines = 9
        line_x_coordinates = np.linspace(0, width, num_x_lines, dtype=int)

        # Draw vertical lines on both frames
        for x in line_x_coordinates:
            cv2.line(frame1, (x, 0), (x, height), (0, 0, 255), 1)  # Red vertical lines on the first frame
            cv2.line(frame2, (x, 0), (x, height), (0, 0, 255), 1)  # Red vertical lines on the second frame

        # Calculate the y-coordinates of the 23 equidistant horizontal lines
        num_y_lines = 23
        line_y_coordinates = np.linspace(0, height, num_y_lines, dtype=int)

        # Draw horizontal lines on both frames
        for y in line_y_coordinates:
            cv2.line(frame1, (0, y), (width, y), (0, 255, 0), 1)  # Green horizontal lines on the first frame
            cv2.line(frame2, (0, y), (width, y), (0, 255, 0), 1)  # Green horizontal lines on the second frame

        # Draw circles at the intersections of vertical and horizontal lines at alternate positions
        for x in range(len(line_x_coordinates)):
            for y in range(len(line_y_coordinates)):
                if (x) % 2 == 0 and (y) % 3 == 0:
                    cv2.circle(frame1, (line_x_coordinates[x], line_y_coordinates[y]), 3, (255, 0, 0), 1)  # Blue circles on the first frame
                    cv2.circle(frame2, (line_x_coordinates[x], line_y_coordinates[y]), 3, (255, 0, 0), 1)  # Blue circles on the second frame

        cv2.circle(frame1, (line_x_coordinates[num_x_lines//2], line_y_coordinates[num_y_lines//2]), 3, (0, 0, 0), -1)  # Black-filled circle on the first frame
        cv2.circle(frame2, (line_x_coordinates[num_x_lines//2], line_y_coordinates[num_y_lines//2]), 3, (0, 0, 0), -1)  # Black-filled circle on the second frame

        cv2.circle(frame1, (line_x_coordinates[num_x_lines//2], line_y_coordinates[num_y_lines//2]), 5, (0, 0, 0), 1)  # Black circle outline on the first frame
        cv2.circle(frame2, (line_x_coordinates[num_x_lines//2], line_y_coordinates[num_y_lines//2]), 5, (0, 0, 0), 1)  # Black circle outline on the second frame

        # Create a new frame with both frames side by side
        combined_frame = cv2.hconcat([frame1, frame2])

        # Display the combined frame
        cv2.imshow('Frames with Vertical and Horizontal Lines', combined_frame)

        # Exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture objects and close the OpenCV windows
    cap1.release()
    # cap2.release()
    cv2.destroyAllWindows()
