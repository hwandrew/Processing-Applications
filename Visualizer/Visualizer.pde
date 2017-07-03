import ddf.minim.analysis.*;
import ddf.minim.*;

Minim minim_;
AudioPlayer audioPlayer_;
FFT fftLin_;
BeatDetect beat_;

float spectrumScale_ = 18;

AudioPlayer[] audioArray_;
int songAmount_ = 5;
int songNumber_ = 0;

void setup() {
  size(1280, 800);
  background(0, 0, 0);
  
  minim_ = new Minim(this);
  
  audioArray_ = new AudioPlayer[songAmount_];
  
  audioArray_[0] = minim_.loadFile("Dont Let Me Go (Echos Remix).mp3");
  audioArray_[1] = minim_.loadFile("Cosmic Love (Seven Lions Remix).mp3");
  audioArray_[2] = minim_.loadFile("The Fall.mp3");
  audioArray_[3] = minim_.loadFile("Days to Come.mp3");
  audioArray_[4] = minim_.loadFile("Mammoth.mp3");

  audioPlayer_ = audioArray_[songNumber_];
  audioPlayer_.play();
  audioPlayer_.loop();
  
  fftLin_ = new FFT(audioPlayer_.bufferSize(),
                    audioPlayer_.sampleRate());
  
  fftLin_.linAverages(30);
}

void draw() {
  fill(135, 240, 250);
  noStroke();
  rect(0, 0, width, height);
  
  fftLin_.forward(audioPlayer_.mix);
  
  noFill();
  
  for (int i = 0; i < fftLin_.avgSize(); i++){
    stroke(236, 0, 140, 0 + fftLin_.getBand(i)*3);
    strokeWeight(0 + (fftLin_.getBand(i/2)));
    ellipse(width/2, height/2, 0 + fftLin_.getAvg(i)*spectrumScale_,
            0 + fftLin_.getAvg(i)*spectrumScale_);
  }
  println(fftLin_.avgSize());
  
  strokeWeight(1.5);
  for(int i = 0; i < audioPlayer_.bufferSize() - 1; i++)
  {
   float x1 = map( i, 0, audioPlayer_.bufferSize(), 0, width );
   float x2 = map( i+1, 0, audioPlayer_.bufferSize(), 0, width );
   stroke(254, 255, 50);
   line( x1, 75 + audioPlayer_.left.get(i)*50, 
         x2, 75 + audioPlayer_.left.get(i+1)*50 );
   line( x1, 725 + audioPlayer_.right.get(i)*50, 
         x2, 725 + audioPlayer_.right.get(i+1)*50 );
   stroke(236, 0, 140);
   line( x1, 50 + audioPlayer_.left.get(i)*50, 
         x2, 50 + audioPlayer_.left.get(i+1)*50 );
   line( x1, 750 + audioPlayer_.right.get(i)*50, 
         x2, 750 + audioPlayer_.right.get(i+1)*50 );
  }
  fill(255);
}



void keyPressed() {
  if (keyPressed) {
    if ((keyCode == UP) && (audioPlayer_.isPlaying())) {
      audioPlayer_.pause();
    } else if (keyCode == RIGHT) {
      audioPlayer_.pause();
      songNumber_ += 1;
      if (songNumber_ == songAmount_) {
        songNumber_ = 0;
      }
      audioPlayer_ = audioArray_[songNumber_];
      audioPlayer_.play();
      audioPlayer_.loop();
    } else if (keyCode == LEFT) {
      audioPlayer_.pause();
      songNumber_ -= 1;
      if (songNumber_ == -1) {
        songNumber_ = songAmount_ - 1;
      }
      audioPlayer_ = audioArray_[songNumber_];
      audioPlayer_.play();
      audioPlayer_.loop();
    } else if (keyCode == UP) {
      audioPlayer_.loop();
    }
  }
}