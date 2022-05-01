// show.h

#ifndef _SHOW_H_
#define _SHOW_H_
#include "episode.h"

class Show
{
  public:
    Show();
    ~Show();

  private:
    char m_title[32];

  struct Season
  {
    int m_num;
    Episode episodes[32];
  };

};

#endif // _SHOW_H_
