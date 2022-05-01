// video.h 

#ifndef _VIDEO_H_
#define _VIDEO_H_

class Video
{
  public:
    Video();
    virtual ~Video();

    void Play();

  private:
    char m_filename[32];
};

#endif // _VIDEO_H_
